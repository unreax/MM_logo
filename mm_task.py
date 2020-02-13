class Draw_MM(object):
    def __init__(self, width_parameter):
        self.n= width_parameter
        
    def error_check(self):
        # Check is parameter valid number for the application
        if (self.n<=2 or self.n>=10000) or self.n%2!=1: return True

    def drawing(self):
        # Main drawing function. It draws M letter multiplied by 2.
        first_row= (('-'*self.n + '*'*self.n)*2 + '-'*self.n)*2 #First and last rows are similar. 
        last_row= (('*'*self.n + '-'*self.n)*2 + '*'*self.n)*2
        
        first_and_last_dash = self.n-1  #Number of '-' in begining and end of M letter
        fisrt_and_last_stars= self.n+2  #Number of '*' in body of M letter
        middle_dashes       = self.n-2  #Number of '-' in the middle ot M letter
        
        print(first_row)
        
        #This loop prints first half of MM
        for row in range((self.n-1)/2):
            print(  '-'*first_and_last_dash     + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*middle_dashes           + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*first_and_last_dash
                    ) * 2
            
            first_and_last_dash = first_and_last_dash - 1
            fisrt_and_last_stars= fisrt_and_last_stars + 2
            middle_dashes       = middle_dashes - 2

        fisrt_and_last_stars= self.n
        middle_stars        = (self.n*2)-1  #Number of '*' in the middle of M letter
        middle_dashes      = 1
        
        #This loop prints second half of MM
        for row in range((self.n-1)/2):
            print(  '-'*first_and_last_dash     + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*middle_dashes           + 
                    '*'*middle_stars            + 
                    '-'*middle_dashes           + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*first_and_last_dash
                    ) * 2
            
            first_and_last_dash = first_and_last_dash - 1
            middle_dashes       = middle_dashes + 2
            middle_stars        = middle_stars - 2
            
        print(last_row)

if __name__ == '__main__':
    parameter= input('Enter width parameter: ')
    application= Draw_MM(parameter)
    if not application.error_check(): application.drawing() #If no error
    else: print('Parameter must be odd number between(and not equal) 2 and 10000!') #If error