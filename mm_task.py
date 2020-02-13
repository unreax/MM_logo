class Draw_MM(object):
    def __init__(self, width_parameter):
        self.n= width_parameter

    def drawing(self):
        # Main drawing function. It draws M letter multiplied by 2.
        
        first_and_last_dash = self.n  #Number of '-' in begining and end of M letter
        fisrt_and_last_stars= self.n  #Number of '*' in body of M letter
        middle_dashes       = self.n  #Number of '-' in the middle ot M letter
        
        #This loop prints first half of MM
        for row in range((self.n+1)/2):
            print(  '-'*first_and_last_dash     + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*middle_dashes           + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*first_and_last_dash
                    ) * 2
            
            first_and_last_dash -= 1
            fisrt_and_last_stars+= 2
            middle_dashes       -= 2

        fisrt_and_last_stars= self.n
        middle_stars        = (self.n*2)-1  #Number of '*' in the middle of M letter
        middle_dashes       = 1
        
        #This loop prints second half of MM
        for row in range((self.n+1)/2):
            print(  '-'*first_and_last_dash     + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*middle_dashes           + 
                    '*'*middle_stars            + 
                    '-'*middle_dashes           + 
                    '*'*fisrt_and_last_stars    + 
                    '-'*first_and_last_dash
                    ) * 2
            
            first_and_last_dash -= 1
            middle_dashes       += 2
            middle_stars        -= 2

def enter_parameter():
    # Check is parameter valid number for the application
    try: 
        n= int(raw_input('Enter width parameter: '))
        if (n<=2 or n>=10000) or n%2==0: 
            print('Parameter must be odd number between(and not equal) 2 and 10000!')
            return enter_parameter()
        else: 
            return n
    except ValueError: 
        print('Please enter a whole number!')
        return enter_parameter()

if __name__ == '__main__':
    parameter   = enter_parameter()
    application = Draw_MM(parameter)
    application.drawing()
