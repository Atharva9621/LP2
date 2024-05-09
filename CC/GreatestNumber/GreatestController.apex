public class GreatestController {
    public Integer num1{get; set;}
    public Integer num2{get; set;}
    public Integer num3{get; set;}
    public Integer greatest{get; set;}
    
    public GreatestController(){
        num1=0;
        num2=0;
        num3=0;
        greatest=0;
    }
    
    public void calculateGreatest(){
        greatest = GreatestNumber.findGreatest(num1, num2, num3);
    }
}