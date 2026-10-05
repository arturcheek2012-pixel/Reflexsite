#import <Foundation/Foundation.h>

%hook UIApplication

- (void)applicationDidFinishLaunching:(UIApplication *)application {
    NSLog(@"[TestTweak] Приложение запущено! Dylib работает.");
    %orig;
}

%end
