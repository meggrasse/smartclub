//
//  SRBeaconManager.h
//  SocialRetailSDK
//
//  Created by vasi on 17/02/15.
//  Copyright (c) 2015 DigitalSocialRetail. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "SRBeaconDelegate.h"
#import <CoreLocation/CoreLocation.h>

@interface SRBeaconManager : NSObject <CLLocationManagerDelegate>

@property(nonatomic,strong)CLBeaconRegion * beaconRegion;
@property(nonatomic,assign)BOOL appClosed;
@property(nonatomic,assign)BOOL adViewOpened;
@property(nonatomic,assign)BOOL appInBackground;

@property(nonatomic,strong)NSString * deviceID;
@property (nonatomic,strong) NSString *uuidCurrent;
@property (nonatomic,strong) NSString *minor;
@property (nonatomic,strong) NSString * major;
@property (nonatomic,strong) NSString * timestamp;

+ (id)sharedManager;
-(void)stopLocation;
-(void)startBeconDetection;
-(void)setBeaconDelegate:(id<SRBeaconDelegate>) beaconDelegate;
-(void)showNotificationWithUserInfo:(NSDictionary*)userInfo state:(UIApplicationState)active;

-(void)willResignActive;
-(void)willTerminate;
-(void)didBecomeActive;
-(void)SetExtraParamsObj:(NSMutableDictionary *)extraParams;
@property(nonatomic,strong)CLBeaconRegion * beaconRegionT;
-(NSDictionary*)GetNearestBeacon;

@end
