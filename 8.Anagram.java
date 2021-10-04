import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
      
        int La = a.length(), Lb = b.length(), ch, i;
      
        a = a.toLowerCase();
        b = b.toLowerCase();
      
        int B[];
        B = new int[26];
      
        for(i=0;i<26;i++){
            B[i] = 0;
            }
              
        if (La == Lb){
            for(i=0; i<La; i++){
                ch = a.charAt(i);
                ch -= 97;
                B[ch] += 1;
            }
            for(i=0; i<Lb; i++){
                ch = b.charAt(i);
                ch -= 97;
                B[ch] -= 1;
            }
            for(i=0;i<26;i++){
                if(B[i] != 0){
                    return false;
                }
            }
            return true;
        }
      
        else{
            return false;
        }
    }
