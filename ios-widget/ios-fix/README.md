# iOS 27 launch crash fix (App Review rejection 2026-10-23, Guideline 2.1(a))

Crash: EXC_BREAKPOINT in `___UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption`
on iPadOS 27.0.1. Apps built with the iOS 27 SDK must adopt the UIScene lifecycle.

Fix on the Mac (ios-widget/ios/App/App):
1. Add `SceneDelegate.swift` (this folder) to the App target.
2. Paste `scene_manifest.plist.xml` into App/Info.plist (inside the top-level <dict>).
   Keep UIMainStoryboardFile = Main.
3. In AppDelegate.swift add:
   func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
       let c = UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
       c.delegateClass = SceneDelegate.self
       return c
   }
4. Bump build to 2 (1.0 (2)), test in an iOS 27 simulator on iPhone and iPad, archive, upload.
5. Capacitor's WidgetBridge plugin (MyViewController) must still be the storyboard root controller.
