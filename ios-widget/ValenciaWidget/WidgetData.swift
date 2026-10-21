import Foundation

/// Shared between the app (WidgetBridgePlugin) and the widget extension.
/// Add this file to BOTH targets.
enum WidgetShared {
    static let appGroup = "group.com.diusialvalencia.app"
    static let key = "widgetData"
    static let revealKey = "wordRevealed"
    static var defaults: UserDefaults { UserDefaults(suiteName: appGroup) ?? .standard }
}

struct WidgetData: Codable {
    var streak: Int = 0
    var xp: Int = 0
    var leaves: Int = 0
    var lastLessonDate: String = ""      // "YYYY-MM-DD" in Europe/Madrid
    var nextLessonTitle: String = "Hola i adéu"
    var nextLessonId: String = ""
    var wordVa: String = "Bon dia"
    var wordEs: String = "Buenos días"
    var updatedAt: Double = 0

    static func load() -> WidgetData {
        guard let d = WidgetShared.defaults.data(forKey: WidgetShared.key),
              let v = try? JSONDecoder().decode(WidgetData.self, from: d) else { return WidgetData() }
        return v
    }

    static var todayKey: String {
        let f = DateFormatter()
        f.calendar = Calendar(identifier: .gregorian)
        f.timeZone = TimeZone(identifier: "Europe/Madrid")
        f.dateFormat = "yyyy-MM-dd"
        return f.string(from: Date())
    }
    var doneToday: Bool { lastLessonDate == WidgetData.todayKey }
}
