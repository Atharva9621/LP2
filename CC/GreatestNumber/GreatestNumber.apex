public class GreatestNumber{
    public static integer findGreatest(integer x1, integer x2, integer x3){
        integer res = x1;
        if(x2>res){
            res = x2;
        }
        if(x3>res){
            res = x3;
        }
        return res;
    }     
}
integer greatest = GreatestNumber.findGreatest(10, 25, 19);
System.debug('The largest value is' + greatest);