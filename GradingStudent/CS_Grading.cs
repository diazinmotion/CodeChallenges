/**
 * Ini merupakan aplikasi sample dari challange hackerrank
 * dengan judul Grading Students oleh nabila_ahmed.
 *
 * @author  Dimas
 * @version 1.0
 * @since   2018-02-09
 * @see     https://www.hackerrank.com/challenges/grading/problem    
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GradingStudent
{
    class Program
    {
        static int schoolPG = 40; // Passing Grade

        static void Main(string[] args){
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
                List<int> hasilPembulatan = pembulatan(schoolPG, 5, 100, nilaiInputan);

                // tampilkan nilai awal dan nilai akhir siswa
                Console.WriteLine("\nFinal Score:");
                for (int index = 0; index < nilaiInputan.Length; index++) {
                    string status = "Lulus";
                    if (hasilPembulatan[index] < schoolPG) {
                        status = "Gagal";
                    }

                    Console.WriteLine("Siswa ke-{0}: {1} --> {2} ({3})", (index + 1), nilaiInputan[index], hasilPembulatan[index], status);
                }
            }

            Console.Write("\nTerminating Application...");
            Console.ReadKey();
        }

        static List<int> pembulatan(int passingGrade, int roundingStepValue, int maxScore, int[] studentGrade){
            List<int> nilaiAkhir = new List<int>();
            List<int> daftarPembulatan = new List<int>();

            // nilai-nilai batas hasil pembulatan dari passingGrade ke maxScore
            for (int i = passingGrade; i <= maxScore; i += roundingStepValue) {
                daftarPembulatan.Add(i);
            }
            
            foreach (int grade in studentGrade) {
                // nilai yang kurang dari 3 dari passing grade bisa dibulatkan 
                // dan dianggap lulus. kurang dari passing grade tidak perlu di bulatkan karena tidak lulus.
                if(grade >= (passingGrade - 3)) {
                    // bandingkan nilai dengan daftar pembulatan nilai
                    foreach(int nilaiBulat in daftarPembulatan) {
                        // bandingkan nilai dengan nilai pembulatan yang lebih besar dari nilai siswa, dan
                        // bila jumlah pengurangan nilai pembulatan dan batas pembulatan terdekat <= 3
                        if (nilaiBulat >= grade) {
                            if ((nilaiBulat - grade) <= 3) {
                                nilaiAkhir.Add(nilaiBulat);
                            } else {
                                nilaiAkhir.Add(grade);
                            }
                            break;
                        }
                    }
                } else {
                    // nilai rendah < 40 dan tidak akan mencapai 40 setelah pembulatan.
                    // tidak perlu di rounding.
                    nilaiAkhir.Add(grade);
                }
            }

            return nilaiAkhir;
        }

        static int inputanAngka(string message, int minValue = 0, int maxValue = 100) {
            int outputValue = 0;
            string pesanError = null;
            bool isValid = false;

            // bila inputan user belum ada atau tidak valid, 
            // looping hingga inputan sesuai dengan kriteria (numeric & lbh dari 0)
            while (outputValue <= minValue && ! isValid) {
                Console.Write("{0} ({1} - {2}): ", message, minValue, maxValue);

                string inputanUser = Console.ReadLine();
                // Validasi tipe inputan user adalah integer dan bernilai lebih dari 0
                if (int.TryParse(inputanUser, out outputValue)) {
                    isValid = true;
                    outputValue = int.Parse(inputanUser);
                } else {
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
                    Console.WriteLine("Invalid Entry! {0}", pesanError + "\n");

                    // set outputValue ke 0 (karena inputan tidak sesuai)
                    outputValue = 0;
                }
            }

            return outputValue;
        }
    }
}
