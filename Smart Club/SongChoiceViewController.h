//
//  SongChoiceViewController.h
//  Smart Club
//
//  Created by Meg Grasse on 5/24/16.
//  Copyright © 2016 Meg Grasse. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <SocialRetailSRSDK/SRBeaconDelegate.h>
#import <SocialRetailSRSDK/SRBeaconManager.h>
#import <SocialRetailSRSDK/SRWebViewController.h>

@interface SongChoiceViewController : UIViewController <SRBeaconDelegate>

- (NSString *)sendDataTo:(NSString *)endpoint;


@end
