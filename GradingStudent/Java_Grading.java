import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Ini merupakan aplikasi sample dari challange hackerrank
 * dengan judul Grading Students oleh nabila_ahmed.
 *
 * @author  Dimas
 * @version 1.0
 * @since   2018-02-12
 * @see     https://www.hackerrank.com/challenges/grading/problem    
 */

public class Java_Grading {
	
	static int schoolPG = 40; // Passing Grade
	
	public static void main(String[] args) throws IOException {
		int jumlah = 0, nilai;
		jumlah = inputanAngka("Jumlah Siswa", 0, 100);
		
		if(jumlah > 0) {
			int[] nilaiInputan = new int[jumlah];
			
			for(int i = 1; i <= jumlah; i++) {
                nilai = inputanAngka("Nilai siswa ke-" + i, 0, 100);

                if(nilai >= 0) {
                    nilaiInputan[(i - 1)] = nilai;
                }
            }
			
			// masukkan ke variabel hasil pembulatan nilai siswa
            List<Integer> hasilPembulatan = pembulatan(schoolPG, 5, 100, nilaiInputan);
            
            // tampilkan nilai awal dan nilai akhir siswa
            System.out.println("\nFinal Score:");
            for (int index = 0; index < nilaiInputan.length; index++) {
                String status = "Lulus";
                if (hasilPembulatan.get(index) < schoolPG) {
                    status = "Gagal";
                }

                System.out.printf("Siswa ke-%d: %d --> %d (%s)\n", (index + 1), nilaiInputan[index], hasilPembulatan.get(index), status);
            }
		}
		
		System.out.print("\nTerminating Application...");
		System.in.read();
	}
	
	public static List<Integer> pembulatan(int passingGrade, int roundingStepValue, int maxScore, int[] studentGrade){
		List<Integer> nilaiAkhir = new ArrayList<Integer>();
		List<Integer> daftarPembulatan = new ArrayList<Integer>();
		
		// nilai-nilai batas hasil pembulatan dari passingGrade ke maxScore
        for (int i = passingGrade; i <= maxScore; i += roundingStepValue) {
            daftarPembulatan.add(i);
        }
        
        for (int grade : studentGrade) {
            // nilai yang kurang dari 3 dari passing grade bisa dibulatkan 
            // dan dianggap lulus. kurang dari passing grade tidak perlu di bulatkan karena tidak lulus.
            if(grade >= (passingGrade - 3)) {
                // bandingkan nilai dengan daftar pembulatan nilai
                for(int nilaiBulat : daftarPembulatan) {
                    // bandingkan nilai dengan nilai pembulatan yang lebih besar dari nilai siswa, dan
                    // bila jumlah pengurangan nilai pembulatan dan batas pembulatan terdekat <= 3
                    if (nilaiBulat >= grade) {
                        if ((nilaiBulat - grade) <= 3) {
                            nilaiAkhir.add(nilaiBulat);
                        } else {
                            nilaiAkhir.add(grade);
                        }
                        break;
                    }
                }
            } else {
                // nilai rendah < 40 dan tidak akan mencapai 40 setelah pembulatan.
                // tidak perlu di rounding.
                nilaiAkhir.add(grade);
            }
        }
        
        return nilaiAkhir;
	}
	
	public static int inputanAngka(String message, int minValue, int maxValue) {
		int outputValue = 0;
        String pesanError = null;
        Boolean isValid = false;
        
        // bila inputan user belum ada atau tidak valid, 
        // looping hingga inputan sesuai dengan kriteria (numeric & lbh dari 0)
        while (outputValue <= minValue && ! isValid) {
            System.out.printf("%s (%d - %d): ", message, minValue, maxValue);
            
            // baca inputan dari user
            Scanner sc = new Scanner(System.in);
            
            String inputanUser = sc.nextLine();
            
            // Validasi tipe inputan user adalah integer dan bernilai lebih dari 0
            try {
            	isValid = true;
                outputValue = Integer.parseInt(inputanUser);
            }catch(NumberFormatException e) {
            	isValid = false;
                pesanError = "Hanya dapat memproses angka saja.";
            }
            
            // apabila inputan user melebihi dari batas atas yang ditentukan
            if(outputValue > maxValue) {
                isValid = false;
                pesanError = "Inputan melebihi batas atas kriteria (max. " + maxValue + ").";
            }

            // apabila inputan user kurang dari batas bawah yang ditentukan
            if (outputValue < minValue) {
                isValid = false;
                pesanError = "Inputan kurang dari batas bawah kriteria (min. " + minValue + ").";
            }

            // tampilkan pesan error umum terhadap inputan user
            if(! isValid) {
                System.out.printf("\nInvalid Entry! %s", pesanError + "\n");

                // set outputValue ke 0 (karena inputan tidak sesuai)
                outputValue = 0;
            }
        }
        
		return outputValue; 
	}
}
