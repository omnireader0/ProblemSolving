package Java.This_is_codingtest.implementation.PRG_자물쇠와열쇠;

public class Main2 {
    public boolean solution(int[][] key, int[][] lock) {
        
        int lockLen = lock.length;
        int keyLen = key.length;
        int [][] copyLock = new int[lockLen + keyLen * 2][lockLen + keyLen * 2]; 

        for (int i = 0; i < lockLen; i++){
            for (int j = 0; j < lockLen; j++){
                copyLock[i + keyLen][j + keyLen] = lock[i][j]; 
            }
        } // 기존의 자물쇠를 새로운 자물쇠 중앙에 배치
        
        for (int r=0; r<4; r++){
            key = rotate(key);
            if(isPossible(key, copyLock)) return true;
        }
        return false;
    }
    
    private boolean isPossible(int[][] key, int[][] copyLock) {
        
        int moveLen = copyLock.length - key.length; // key가 새 자물쇠에 이동할 수 있는 길이
        for(int i = 0; i < moveLen; i++) {
            for (int j = 0; j < moveLen; j++) {
                if(check(i, j, key, copyLock)) return true;
            }
        }
        return false;
    } // 새 자물쇠에 key를 끼울 수 있는지 검사
    
    private boolean check(int x, int y, int[][] key, int[][] copyLock) {
        
        int copyLen = copyLock.length;
        int keyLen = key.length;
        int[][] copy = new int[copyLen][copyLen];
        
        for (int i = 0; i < copyLen; i++){
            copy[i] = copyLock[i].clone();
        }
        
        for (int i=0; i < keyLen; i++){
            for (int j=0; j < keyLen; j++){
                copy[i + x][j + y] += key[i][j];
            }
        }
        
        for (int i = keyLen; i < copyLen - keyLen; i++) {
            for (int j = keyLen; j < copyLen - keyLen; j++) {
                if(copy[i][j] != 1) return false;
            }
        }
        return true;
    }// 검사하는 방법 : 새로운 자물쇠 중앙 부분이 1인지 확인
    
    private int[][] rotate(int[][] key) {

        int keyLen = key.length;
        int[][] copy = new int[keyLen][keyLen];
        
        for (int i = 0; i < keyLen; i++){
            for (int j = 0; j < keyLen; j++) {
                copy[i][j] = key[keyLen -1 -j][i];
            }
        }
        return copy;
    } // key를 시계방향으로 90도 회전
}
