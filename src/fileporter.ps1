$hash = @{"AR"="ar";"BR"="pt-BR";"CR"="hr";"CZ"="cs";"DK"="da";
			"FI"="fi";"FR"="fr";"GK"="el";"GR"="de";"HE"="he";
			"HU"="hu";"IT"="it";"JP"="ja";"KR"="ko";"NL"="nl";
			"NO"="nb";"PL"="pl";"PO"="pt";"RO"="ro";"RU"="ru";
			"SC"="zh-Hans";"SH"="sr-Latn";"SK"="sk";"SL"="sl";
			"SP"="es";"SV"="sv";"TC"="zh-Hant";"TU"="tr";"UA"="uk"}
Get-ChildItem ./ | ForEach-Object -Process{
	if($_-is [System.IO.DirectoryInfo]){
		if($hash.contains($_.name)){
			if(-not (Test-path json)){
				mkdir json
			}
			$old_path = $_.name+"/en.json"
			if(-not (Test-path $old_path)){
				$old_path = $_.name+"/"+$hash[$_.name]+".json"
			}
			if(-not (Test-path $old_path)){
				$old_path = $_.name+"/"+$_.name+".json"
			}
			if(Test-path $old_path){
				$new_path = "json/"+$hash[$_.name]+".json"
				Move-Item $old_path $new_path
				Remove-Item $_.name
			}
		}
	}
}