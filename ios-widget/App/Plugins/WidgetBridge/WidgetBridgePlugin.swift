import Foundation
import Capacitor
import WidgetKit

/// JS: Capacitor.Plugins.WidgetBridge.update({...}) — App target only.
/// Also add ValenciaWidget/WidgetData.swift to the App target.
@objc(WidgetBridgePlugin)
public class WidgetBridgePlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "WidgetBridgePlugin"
    public let jsName = "WidgetBridge"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "update", returnType: CAPPluginReturnPromise)
    ]

    @objc func update(_ call: CAPPluginCall) {
        var d = WidgetData.load()
        d.streak = call.getInt("streak") ?? d.streak
        d.xp = call.getInt("xp") ?? d.xp
        d.leaves = call.getInt("leaves") ?? d.leaves
        d.lastLessonDate = call.getString("lastLessonDate") ?? d.lastLessonDate
        d.nextLessonTitle = call.getString("nextLessonTitle") ?? d.nextLessonTitle
        d.nextLessonId = call.getString("nextLessonId") ?? d.nextLessonId
        let newWord = call.getString("wordVa") ?? d.wordVa
        if newWord != d.wordVa { WidgetShared.defaults.set(false, forKey: WidgetShared.revealKey) } // new day, hide again
        d.wordVa = newWord
        d.wordEs = call.getString("wordEs") ?? d.wordEs
        d.updatedAt = Date().timeIntervalSince1970
        if let blob = try? JSONEncoder().encode(d) { WidgetShared.defaults.set(blob, forKey: WidgetShared.key) }
        WidgetCenter.shared.reloadAllTimelines()
        call.resolve(["ok": true])
    }
}
