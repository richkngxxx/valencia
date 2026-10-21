import WidgetKit
import SwiftUI
import AppIntents

// MARK: - Brand
extension Color {
    static let brandGreen = Color(red: 0x58/255, green: 0xCC/255, blue: 0x02/255)
    static let brandGreenDark = Color(red: 0x46/255, green: 0xA3/255, blue: 0x02/255)
    static let leafOrange = Color(red: 0xF2/255, green: 0x8C/255, blue: 0x28/255)
    static let flame = Color(red: 0xFF/255, green: 0x96/255, blue: 0x00/255)
    static let navy = Color(red: 0x1B/255, green: 0x25/255, blue: 0x4B/255)
    static let sky = Color(red: 0x1C/255, green: 0xB0/255, blue: 0xF6/255)
}

// MARK: - Timeline
struct Entry: TimelineEntry {
    let date: Date
    let data: WidgetData
    let revealed: Bool

    /// sleep if nothing done today (late in the day), cheer if done, neutral otherwise
    var pose: String {
        if data.doneToday { return "BatCheer" }
        let h = Calendar.current.component(.hour, from: date)
        return (h >= 20 || h < 7) ? "BatSleep" : (h >= 16 ? "BatSad" : "BatNeutral")
    }
    var greeting: String {
        let h = Calendar.current.component(.hour, from: date)
        switch h {
        case 6..<13: return "Bon dia!"
        case 13..<20: return "Bona vesprada!"
        default: return "Bona nit!"
        }
    }
    var nudge: String {
        if data.doneToday { return "Lliçó d'avui feta! 🎉" }
        if data.streak == 0 { return "Comencem una ratxa?" }
        let h = Calendar.current.component(.hour, from: date)
        return h >= 18 ? "Que no se t'escape la ratxa!" : "Has fet la lliçó d'avui?"
    }
}

struct Provider: TimelineProvider {
    func placeholder(in context: Context) -> Entry { Entry(date: .now, data: WidgetData(streak: 7, xp: 320), revealed: false) }
    func getSnapshot(in context: Context, completion: @escaping (Entry) -> Void) {
        completion(context.isPreview ? placeholder(in: context) : current())
    }
    func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> Void) {
        // one entry now + one per hour for 6h so greeting/pose follow the clock; then ask again
        let now = Date(), d = WidgetData.load(), rev = WidgetShared.defaults.bool(forKey: WidgetShared.revealKey)
        let start = Calendar.current.dateInterval(of: .hour, for: now)?.start ?? now
        var entries = [Entry(date: now, data: d, revealed: rev)]
        for i in 1...6 { entries.append(Entry(date: start.addingTimeInterval(Double(i) * 3600), data: d, revealed: rev)) }
        completion(Timeline(entries: entries, policy: .after(start.addingTimeInterval(3600))))
    }
    private func current() -> Entry {
        Entry(date: .now, data: WidgetData.load(), revealed: WidgetShared.defaults.bool(forKey: WidgetShared.revealKey))
    }
}

// MARK: - Intents (iOS 17 interactive widgets)
struct ToggleWordIntent: AppIntent {
    static var title: LocalizedStringResource = "Mostrar traducció"
    func perform() async throws -> some IntentResult {
        let d = WidgetShared.defaults
        d.set(!d.bool(forKey: WidgetShared.revealKey), forKey: WidgetShared.revealKey)
        return .result()   // WidgetKit reloads the timeline after an intent runs
    }
}

// MARK: - Views
struct FlameBadge: View {
    let n: Int; let size: CGFloat
    var body: some View {
        HStack(spacing: 4) {
            Image(systemName: "flame.fill").font(.system(size: size * 0.8, weight: .bold)).foregroundStyle(n > 0 ? Color.flame : .white.opacity(0.5))
            Text("\(n)").font(.system(size: size, weight: .black, design: .rounded)).foregroundStyle(.white)
                .minimumScaleFactor(0.5).lineLimit(1)
        }
    }
}

struct SmallView: View {
    let e: Entry
    var body: some View {
        ZStack(alignment: .bottomTrailing) {
            VStack(alignment: .leading, spacing: 2) {
                FlameBadge(n: e.data.streak, size: 40)
                Text(e.data.streak == 1 ? "dia de ratxa" : "dies de ratxa").font(.system(size: 13, weight: .heavy, design: .rounded)).foregroundStyle(.white.opacity(0.9))
                Spacer()
            }.frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
            Image(e.pose).resizable().scaledToFit().frame(width: 84, height: 84).offset(x: 10, y: 18)
        }
        .widgetURL(URL(string: "diusialvalencia://lesson/next"))
    }
}

struct MediumView: View {
    let e: Entry
    var body: some View {
        HStack(spacing: 10) {
            VStack(alignment: .leading, spacing: 4) {
                Text(e.greeting).font(.system(size: 20, weight: .black, design: .rounded)).foregroundStyle(.white)
                HStack(spacing: 10) {
                    FlameBadge(n: e.data.streak, size: 22)
                    HStack(spacing: 3) {
                        Image(systemName: "bolt.fill").foregroundStyle(.yellow)
                        Text("\(e.data.xp) XP").font(.system(size: 15, weight: .heavy, design: .rounded)).foregroundStyle(.white)
                    }
                }
                Text(e.nudge).font(.system(size: 13, weight: .bold, design: .rounded)).foregroundStyle(.white.opacity(0.92)).lineLimit(1)
                Spacer(minLength: 0)
                Link(destination: URL(string: "diusialvalencia://lesson/next")!) {
                    HStack(spacing: 4) {
                        Text(e.data.doneToday ? "Repassar" : "Practicar").font(.system(size: 14, weight: .black, design: .rounded))
                        Text("· \(e.data.nextLessonTitle)").font(.system(size: 12, weight: .bold, design: .rounded)).lineLimit(1)
                    }
                    .foregroundStyle(Color.brandGreenDark)
                    .padding(.horizontal, 12).padding(.vertical, 7)
                    .background(Capsule().fill(.white))
                }
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            VStack(spacing: 0) {
                Button(intent: ToggleWordIntent()) {
                    VStack(spacing: 2) {
                        Text("Paraula del dia").font(.system(size: 10, weight: .heavy)).foregroundStyle(Color.navy.opacity(0.6))
                        Text(e.data.wordVa).font(.system(size: 15, weight: .black, design: .rounded)).foregroundStyle(Color.navy).minimumScaleFactor(0.6).lineLimit(2)
                        Text(e.revealed ? e.data.wordEs : "Toca per veure-la").font(.system(size: 11, weight: .bold)).foregroundStyle(e.revealed ? Color.sky : Color.navy.opacity(0.45)).lineLimit(2)
                    }
                    .multilineTextAlignment(.center)
                    .padding(8).frame(width: 118, height: 82)
                    .background(RoundedRectangle(cornerRadius: 14).fill(.white))
                }.buttonStyle(.plain)
                Image(e.pose).resizable().scaledToFit().frame(width: 62, height: 62).offset(y: 10)
            }
        }
    }
}

struct ValenciaWidgetView: View {
    @Environment(\.widgetFamily) var family
    let entry: Entry
    var body: some View {
        Group {
            if family == .systemSmall { SmallView(e: entry) } else { MediumView(e: entry) }
        }
        .containerBackground(for: .widget) {
            LinearGradient(colors: [.brandGreen, .brandGreenDark], startPoint: .top, endPoint: .bottom)
        }
    }
}

struct ValenciaWidget: Widget {
    let kind = "ValenciaWidget"
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: Provider()) { ValenciaWidgetView(entry: $0) }
            .configurationDisplayName("Diu sí al valencià")
            .description("La teua ratxa, la paraula del dia i la pròxima lliçó.")
            .supportedFamilies([.systemSmall, .systemMedium])
    }
}

@main
struct ValenciaWidgetBundle: WidgetBundle {
    var body: some Widget { ValenciaWidget() }
}

#Preview(as: .systemMedium) { ValenciaWidget() } timeline: {
    Entry(date: .now, data: WidgetData(streak: 12, xp: 840, leaves: 31, lastLessonDate: "", nextLessonTitle: "La família"), revealed: false)
    Entry(date: .now, data: WidgetData(streak: 13, xp: 870, leaves: 32, lastLessonDate: WidgetData.todayKey, nextLessonTitle: "La família"), revealed: true)
}
