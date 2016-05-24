//
//  WebViewController.h
//  AirCaraibesNew
//
//  Created by Horia Grama on 11/7/12.
//  Copyright (c) 2012 Pirlitu Vasilica. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface SRWebViewController : UIViewController <UIWebViewDelegate>
{
    IBOutlet UIWebView *webView;
}
@property (weak, nonatomic) IBOutlet UINavigationBar *navBar;

@property (weak, nonatomic) IBOutlet UINavigationItem *navItem;
@property (weak, nonatomic) IBOutlet UIButton *goBackBut;
@property(nonatomic,strong)NSString *url;
@property (nonatomic, retain) UIView *viewToReturn;
@property (nonatomic,strong) NSString * strTitle;
@property (weak, nonatomic) IBOutlet UIButton *backBut;

- (IBAction)back:(id)sender;
-(id)initWithLink:(NSString*)link;
-(void)setTitleViewT:(NSString *)title;
-(void)prepareLinkMesVelos:(NSString*)loc1 :(NSString*)loc2;
@property (nonatomic,readwrite) int numberLoads;
@property (nonatomic,strong) NSString * titleOutlet;
@property (weak, nonatomic) IBOutlet UIBarButtonItem *safariBut;
@property (weak, nonatomic) IBOutlet UIBarButtonItem *cancelBut;

@end
