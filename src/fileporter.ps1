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
			$new_path = "json/"+$hash[$_.name]+".json"
			Move-Item $old_path $new_path
			Remove-Item $_.name
		}
	}
}