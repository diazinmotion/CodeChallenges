import 'dart:io';

/**
 * Ini merupakan aplikasi sample dari challange hackerrank
 * dengan judul Grading Students oleh nabila_ahmed.
 *
 * @author  Dimas
 * @version 1.0
 * @since   2020-10-15
 * @see     https://www.hackerrank.com/challenges/grading/problem    
 */

const int passingGrade = 40; // passing grade

main(List<String> args) {
    int nilai       = 0;
    List<int> nilaiInputan  = [];

    final jumlah = inputanAngka('Jumlah Siswa', minValue: 0, maxValue: 100);
    if(jumlah > 0){
        for(var i = 1; i <= jumlah; i++) {
            nilai = inputanAngka("Nilai siswa ke-$i:", minValue: 0, maxValue: 100);

            if(nilai >= 0){
                nilaiInputan.insert((i - 1), nilai);
            }
        }

        List<int> hasilPembulatan = pembulatan(passingGrade, 5, 100, nilaiInputan);
        print('Final Score:');
        for(var i = 0; i < nilaiInputan.length; i++){
            String status = 'Lulus';
            if(hasilPembulatan[i] < passingGrade){
                status = 'Gagal';
            }

            print('Siswa ke-${(i + 1)}: ${nilaiInputan[i]} --> ${hasilPembulatan[i]} ($status)');
        }
    }

    print('Terminating Application...');
}

List<int> pembulatan(int passingGrade, int roundingStepValue, int maxScore, List<int> studentGrade){
    List<int> nilaiAkhir        = [];
    List<int> daftarPembulatan  = [];

    // nilai-nilai batas hasil pembulatan dari passingGrade ke maxScore
    for(var i = passingGrade; i <= maxScore; i+= roundingStepValue){
        daftarPembulatan.add(i);
    }

    for(var grade in studentGrade) {
        // nilai yang kurang dari 3 dari passing grade bisa dibulatkan 
        // dan dianggap lulus. kurang dari passing grade tidak perlu di bulatkan karena tidak lulus.
        if(grade >= (passingGrade - 3)){
            // bandingkan nilai dengan daftar pembulatan nilai
            for(var nilaiBulat in daftarPembulatan) {
                // bandingkan nilai dengan nilai pembulatan yang lebih besar dari nilai siswa, dan
                // bila jumlah pengurangan nilai pembulatan dan batas pembulatan terdekat <= 3
                if(nilaiBulat >= grade){
                    if((nilaiBulat - grade) <= 3){
                        nilaiAkhir.add(nilaiBulat);
                    }else{
                        nilaiAkhir.add(grade);
                    }
                    break;
                }
            }
        }else{
            // nilai rendah < 40 dan tidak akan mencapai 40 setelah pembulatan.
            // tidak perlu di rounding.
            nilaiAkhir.add(grade);
        }
    }

    return nilaiAkhir;
}

int inputanAngka(String message, {int minValue = 0, int maxValue = 100}){

    int outputVal       = 0;
    String pesanError   = null;
    bool isValid        = false;

    while(outputVal <= minValue && ! isValid){
        
        stdout.write('$message ($minValue - $maxValue): ');

        try{
            isValid     = true;
            outputVal   = int.parse(stdin.readLineSync());

            if(outputVal > maxValue){
                isValid     = false; 
                pesanError  = "Inputan melebihi batas atas kriteria (max. " + maxValue.toString() + ").";
            }else if(outputVal < minValue){
                isValid     = false; 
                pesanError  = "Inputan kurang dari batas bawah kriteria (min. " + minValue.toString() + ").";
            }
        }on FormatException{
            isValid     = false; 
            pesanError  = 'Hanya dapat memproses angka saja.';
        }catch (e){
            isValid     = false; 
            pesanError  = 'Unexpected error $e';
        }

        if(! isValid){
            print('Invalid Entry! $pesanError');
        }
    }

    return outputVal;
}