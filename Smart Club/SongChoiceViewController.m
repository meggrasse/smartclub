//
//  SongChoiceViewController.m
//  Smart Club
//
//  Created by Meg Grasse on 5/24/16.
//  Copyright © 2016 Meg Grasse. All rights reserved.
//

#import "SongChoiceViewController.h"

@implementation SongChoiceViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)voteThumbsUp:(UIButton *)sender {
    [self sendDataTo:@"upvote"];
 }

- (IBAction)voteThumbsDown:(UIButton *)sender {
    [self sendDataTo:@"downvote"];
}

-  (NSString *)sendDataTo:(NSString *)endpoint{
    NSString *url = [@"https://smartclub.herokuapp.com/" stringByAppendingString:endpoint];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setHTTPMethod:@"GET"];
    [request setURL:[NSURL URLWithString:url]];
    NSError *error = [[NSError alloc] init];
    NSHTTPURLResponse *responseCode = nil;
    
    NSData *oResponseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&responseCode error:&error]; //probably should update this
    
    if([responseCode statusCode] != 200){
        NSLog(@"Error getting %@, HTTP status code %li", url, (long)[responseCode statusCode]);
        return nil;
    }
    
    return [[NSString alloc] initWithData:oResponseData encoding:NSUTF8StringEncoding];
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
