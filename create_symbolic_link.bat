@echo off

set modName="kaiserreich_traduction_francophone"
set gitModDir=".\Traduction-FR-Kaiserreich"

if not exist %modDir% (
	echo ERROR: HoI4 mod directory not found. Searched repertory : %modDir%.
	goto end
)

if not exist %modDir%\%modName% (
	mklink /J %modDir%\%modName% %gitModDir%
) else (
	echo ERROR: %modDir%\%modName%  already exists
	goto end
)

if not exist %modDir%\%modName%.mod (
	xcopy .\%modName%.mod %modDir%\%modName%.mod*
	echo %modDir%\%modName%.mod
) else (
	echo WARNING: %modDir%\%modName%.mod already exists. Check it has the good content.
	goto end
)

:end
pause