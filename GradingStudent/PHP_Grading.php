<?php
    // Link of challange: https://www.hackerrank.com/challenges/grading/problem
    
	$nilai = [56, 67, 38, 33];

	function multiplikasi($batas_bawah = 0, $batas_atas = 100, $faktorial = 0){
		
		$result = null;

		if($faktorial <= 0){
			$result = false;
		}else{
			// hasil sementara
			$temp_hasil = [];

			for($i = $batas_bawah; $i <= $batas_atas; $i += $faktorial){
				// masukkan ke dalam hasil sementara
				array_push($temp_hasil, $i);
			}

			// masukkan ke dalam variabel akhir
			$result = $temp_hasil;
		}

		return $result;
	}

	function pembulatan($nilai = []){
		
		$result = null;

		if(empty($nilai) && ! is_array($nilai)){
			$result = false;
		}else{
			$temp_hasil = [];

			// dapatkan batas-batas nilai pembulatan
			$batas_pembulatan = multiplikasi(40, 100, 5);

			// looping nilai yang diinput user
			foreach($nilai as $row){
				// yang lebih besar dari 40
				if($row >= 37){
					// bandingkan antara nilai yg dilooping dengan batas pembulatan
					foreach($batas_pembulatan as $row_bulatan){
						if($row_bulatan > $row){
							// bila jumlah pengurangan nilai pembulatan dan batas pembulatan terdekat <= 3
							if($row_bulatan - $row <= 3){
								array_push($temp_hasil, $row_bulatan);
							}else{
								array_push($temp_hasil, $row);
							}
							
							break;
						}	
					}
				}else{
					// nilai rendah < 40 dan tidak akan mencapai 40 setelah pembulatan.
					// tidak perlu di rounding.
					array_push($temp_hasil, $row);
				}
			}

			$result = $temp_hasil;
		}

		return $result;
	}

	$nilai_tampil 	= [];
	$nilai_akhir 	= pembulatan($nilai);

	// execute hasil
	echo "Nilai Awal: <br/>";
	echo implode(", ", $nilai);
	echo "<br/><br/>Nilai Akhir:<br/>";
	foreach($nilai as $key => $row){
		if(isset($nilai_akhir[$key])){
			$no = ($key+1);
			array_push($nilai_tampil, "{$no}. {$row} -> {$nilai_akhir[$key]}<br/>");
		}
	}
	echo implode("", $nilai_tampil);
?>