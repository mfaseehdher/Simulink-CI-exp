model = "add_two_numbers"; 
load_system(model);
outDir = fullfile(pwd, "fmu_out");
if ~exist(outDir, "dir"), mkdir(outDir); end

exportToFMU2CS(model, ...
    'FMUName', 'add_two_numbers_fmu', ...
    'OutputFolder', outDir);

disp("FMU exported to: " + outDir);