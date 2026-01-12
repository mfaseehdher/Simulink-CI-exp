model = "add_two_numbers"; 
load_system(model);

% --- CI-safe: enforce solver settings every time ---
set_param(model, "SolverType", "Fixed-step");
set_param(model, "Solver", "FixedStepDiscrete");  % matches "discrete (no continuous states)"
set_param(model, "FixedStep", "auto");            % or "0.01" etc.

save_system(model);  % IMPORTANT so the configuration is saved before export

outDir = fullfile(pwd, "fmu_out");
if ~exist(outDir, "dir"), mkdir(outDir); end

exportToFMU2CS(model, ...
    'FMUName', 'add_two_numbers_fmu', ...
    'OutputFolder', outDir);

disp("FMU exported to: " + outDir);