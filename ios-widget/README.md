# iOS app + home-screen widget (Capacitor + WidgetKit)

Nothing here changes the PWA. `index.html` only contains a guarded bridge (`widgetSync()`, `appUrlOpen` listener)
that does nothing unless `window.Capacitor.Plugins.WidgetBridge` exists.

## Files
| Path | Target | What |
|---|---|---|
| `capacitor.config.json` | – | appId `com.diusialvalencia.app`, webDir `www` |
| `package.json` | – | Capacitor 7 deps + `npm run sync-web` (copies the PWA into `www/`) |
| `ValenciaWidget/ValenciaWidget.swift` | Widget ext. | Small + medium widgets, hourly timeline, `ToggleWordIntent` (iOS 17 interactive), `Practicar` deep link |
| `ValenciaWidget/WidgetData.swift` | **App + Widget ext.** | Shared Codable model, App Group `group.com.diusialvalencia.app` |
| `ValenciaWidget/Assets.xcassets` | Widget ext. | Bat sprites `BatNeutral/BatCheer/BatSleep/BatSad/BatJump/BatTrophy` (256 px @3x), colours |
| `App/Plugins/WidgetBridge/WidgetBridgePlugin.swift` | App | `WidgetBridge.update({...})` → App Group UserDefaults + `WidgetCenter.reloadAllTimelines()` |
| `App/Plugins/WidgetBridge/MyViewController.swift` | App | Registers the local plugin |
| `preview.html` | – | Mockup source for `_qa/widget-preview.png` |

## 1. Create the Capacitor project (on the Mac)
Needs Xcode 15+, Node 20+, CocoaPods or SPM.
```bash
cd valencia_app/ios-widget
npm install
npm run sync-web            # copies the PWA files into www/
npx cap add ios             # creates ios/App/App.xcodeproj
npx cap sync ios
npx cap open ios
```
The service worker is harmless inside Capacitor (`capacitor://` scheme cannot register it, the app just runs without it).

## 2. Deep link scheme
App target → **Info** → URL Types → **+** → Identifier `com.diusialvalencia.app`, URL Schemes `diusialvalencia`.
Install the App plugin: `npm i @capacitor/app && npx cap sync ios` (already in package.json). The web code listens for
`diusialvalencia://lesson/next` and opens the next unfinished lesson.

## 3. Add the bridge plugin to the App target
1. In Xcode drag `App/Plugins/WidgetBridge/` **and** `ValenciaWidget/WidgetData.swift` into the `App` group. Tick "Copy items if needed" and **Target: App**.
2. Open `App/Main.storyboard` → select *Bridge View Controller* → Identity inspector → Class `MyViewController`, Module `App`.

## 4. Add the Widget Extension target
1. File → New → Target… → **Widget Extension**. Product name `ValenciaWidget`, uncheck "Include Live Activity" and "Include Configuration App Intent". Activate the scheme when asked.
2. Delete the generated `ValenciaWidget.swift`, `ValenciaWidgetBundle.swift`, `AppIntent.swift` and `Assets.xcassets` in the new group.
3. Drag in `ValenciaWidget/ValenciaWidget.swift`, `ValenciaWidget/WidgetData.swift` and `ValenciaWidget/Assets.xcassets` with **Target: ValenciaWidget only** (WidgetData.swift: tick both App and ValenciaWidget).
4. ValenciaWidget target → General → Minimum Deployments **iOS 17.0** (interactive `Button(intent:)` needs 17). Keep the App target at 15+ if you like.

## 5. App Group (both targets)
1. Select the **App** target → Signing & Capabilities → **+ Capability** → **App Groups** → **+** → `group.com.diusialvalencia.app`.
2. Repeat for the **ValenciaWidget** target with the same group (tick it).

## 6. Signing
1. Both targets → Signing & Capabilities → Team = your Apple Developer team, "Automatically manage signing" on.
2. Bundle IDs: App `com.diusialvalencia.app`, widget `com.diusialvalencia.app.ValenciaWidget` (must be a child of the app ID).
3. Xcode registers the App Group on the developer portal automatically; if it fails, create it at developer.apple.com → Identifiers → App Groups, then enable it on both App IDs.

## 7. Run
Pick the **App** scheme, run on a device, open a lesson once (this calls `WidgetBridge.update`), go home, long-press → **+** → "Diu sí al valencià" → small or medium.
To debug the widget, choose the **ValenciaWidget** scheme (it asks which widget family to launch).

## Behaviour
- **Small:** flame + streak number, bat peeking bottom-right. Pose: `BatCheer` if lesson done today, `BatSleep` 20:00–07:00 if not, `BatSad` after 16:00 if not, else `BatNeutral`. Tap → `diusialvalencia://lesson/next`.
- **Medium:** greeting by hour (Bon dia! 6–13 · Bona vesprada! 13–20 · Bona nit!), streak, XP, nudge ("Has fet la lliçó d'avui?" / "Que no se t'escape la ratxa!" / "Lliçó d'avui feta! 🎉"), `Practicar · <next lesson>` link, **Paraula del dia** card: tap flips to the Spanish translation (`ToggleWordIntent`, no app launch). A new word resets it to hidden.
- **Refresh:** timeline has hourly entries for 6 h and `.after(next hour)`; the app calls `reloadAllTimelines()` every time progress is saved.
- **Data written** (JSON under key `widgetData`): `streak, xp, leaves, lastLessonDate (YYYY-MM-DD, Europe/Madrid), nextLessonTitle, nextLessonId, wordVa, wordEs, updatedAt`. Word of the day = deterministic pick from the course's learn cards by date.

## Not done here (needs a Mac)
`npx cap add ios`, building, signing and App Store submission. None of the Swift was compiled on this Linux box; expect to fix small API details in Xcode if any.
