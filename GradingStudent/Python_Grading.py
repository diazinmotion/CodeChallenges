
# Ini merupakan aplikasi sample dari challange hackerrank
# dengan judul Grading Students oleh nabila_ahmed.
#
# @author  Dimas
# @version 1.0
# @since   2020-10-15
# @see     https://www.hackerrank.com/challenges/grading/problem    

_passingGrade = 40

def inputanAngka(msg = None, minValue = 0, maxValue = 0):
    outputVal = 0
    pesanError = None
    isValid = False

    while(outputVal <= minValue and not isValid):
        try:
            isValid = True
            outputVal = int(input('{} ({} - {}): '.format(msg, minValue, maxValue)))

            if outputVal > maxValue:
                isValid     = False
                pesanError  = "Inputan melebihi batas atas kriteria (max. {})".format(maxValue)
            elif outputVal < minValue:
                isValid     = False
                pesanError  = "Inputan kurang dari batas bawah kriteria (min. {})".format(minValue)
        except Exception as e:
            isValid = False
            pesanError = 'Unexpected Error {}'.format(e)

        if not isValid:
            print('Invalid Entry! {}'.format(pesanError))

    return outputVal

def pembulatan(passingGrade, roundingStepValue, maxScore, studentGrade = []):
    nilaiAkhir = []
    daftarPembulatan = []

    for i in range(passingGrade, (maxScore + 1)):
        daftarPembulatan.append(i)
        i += roundingStepValue

    for grade in studentGrade:
        if grade >= (passingGrade - 3):
            for nilaiBulat in daftarPembulatan:
                if nilaiBulat >= grade:
                    if (nilaiBulat - grade) <= 3:
                        nilaiAkhir.append(nilaiBulat)
                    else:
                        nilaiAkhir.append(grade)
                    
                    break
        else:
            nilaiAkhir.append(grade)
    
    return nilaiAkhir

if __name__ == '__main__':
    nilai = 0
    nilaiInputan = []

    jumlah = inputanAngka('Jumlah Siswa', minValue=0, maxValue=100)
    if jumlah >= 0 and jumlah <= 100:
        for i in range(1, (jumlah + 1)):
            nilai = inputanAngka('Nilai siswa ke-{}'.format(i), 0, 100)

            if(nilai >= 0):
                nilaiInputan.insert((i - 1), nilai)

        hasilPembulatan = pembulatan(_passingGrade, 5, 100, nilaiInputan)
        print('Final Score:')

        for i in range(len(nilaiInputan)):
            status = 'Lulus'
            if hasilPembulatan[i] < _passingGrade:
                status = 'Gagal'

            print('Siswa ke-{}: {} --> {} ({})'.format((i + 1), nilaiInputan[i], hasilPembulatan[i], status))

    print('Terminating Application...')