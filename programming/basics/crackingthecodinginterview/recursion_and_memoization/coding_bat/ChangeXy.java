public class ChangeXy {
    public static String changeXY(String str) {
        if (str.length() == 0) {
            return "";
        }
        
        StringBuilder sBuilder = new StringBuilder(
            str.charAt(0) == 'x' ? "y" : str.substring(0, 1));
        sBuilder.append(changeXY(str.substring(1)));
        return sBuilder.toString();
    }
    
    public static void main(String[] args) {
        System.out.println(changeXY("asdx"));
    }
}
