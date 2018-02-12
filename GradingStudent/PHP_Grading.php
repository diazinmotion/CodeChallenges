<?php

    /**
	 * Ini merupakan aplikasi sample dari challange hackerrank
	 * dengan judul Grading Students oleh nabila_ahmed.
	 *
	 * @author  Dimas
	 * @version 1.0
	 * @since   2018-02-12
	 * @see     https://www.hackerrank.com/challenges/grading/problem    
	*/
	namespace GradingStudent;

	class MainApplication {

		private static $schoolPG 	= 40;
		private static $inputanUser	= [56, 67, 38, 33];

		public function runningApp(){

			// dapatkan nilai akhir siswa melalui function yang tersedia
			$nilaiAkhir = self::pembulatan(self::$schoolPG, 5, 100, self::$inputanUser);

			// tampilkan hasil nilai akhir siswa
			print("Final Score: <br/>");
			foreach(self::$inputanUser as $key => $nilai){
				if(isset($nilaiAkhir[$key])){
					printf("%d. Siswa ke-%d: %d --> %d<br/>", ($key + 1), ($key + 1), $nilai, $nilaiAkhir[$key]);
				}
			}

		}

		private static function pembulatan($passingGrade, $roundingStepValue, $maxScore, $studentGrade){
			$nilaiAkhir 		= [];
			$daftarPembulatan 	= [];

			// nilai-nilai batas hasil pembulatan dari passingGrade ke maxScore
            for ($i = $passingGrade; $i <= $maxScore; $i += $roundingStepValue) {
                array_push($daftarPembulatan, $i);
			}
			
			foreach ($studentGrade as $grade) {
				// nilai yang kurang dari 3 dari passing grade bisa dibulatkan 
				// dan dianggap lulus. kurang dari passing grade tidak perlu di bulatkan karena tidak lulus.
				if($grade >= ($passingGrade - 3)) {
					// bandingkan nilai dengan daftar pembulatan nilai
					foreach($daftarPembulatan as $nilaiBulat) {
						// bandingkan nilai dengan nilai pembulatan yang lebih besar dari nilai siswa, dan
						// bila jumlah pengurangan nilai pembulatan dan batas pembulatan terdekat <= 3
						if ($nilaiBulat >= $grade) {
							if (($nilaiBulat - $grade) <= 3) {
								array_push($nilaiAkhir, $nilaiBulat);
							} else {
								array_push($nilaiAkhir, $grade);
							}
							break;
						}
					}
				} else {
					// nilai rendah < 40 dan tidak akan mencapai 40 setelah pembulatan.
					// tidak perlu di rounding.
					array_push($nilaiAkhir, $grade);
				}
			}

			return $nilaiAkhir;
		}

		public static function tes(){
			echo "AAA";
		}
	}

	// Running aplikasi
	\GradingStudent\MainApplication::runningApp();
?>