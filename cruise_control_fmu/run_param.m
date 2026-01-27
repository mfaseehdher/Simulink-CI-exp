t = (0:0.01:120)';     % match your model time
u = 500*ones(size(t)); % constant input

cases = [1000 50; 2000 50; 1000 100];  % [m b]

figure; hold on; grid on;
for i = 1:size(cases,1)
    m = cases(i,1); b = cases(i,2);
    sim('ccmodel');  % uses current m,b,t,u and external input [t,u]
    v_ts = yout.getElement(1).Values;
    plot(v_ts.Time, v_ts.Data, 'DisplayName', sprintf('m=%g, b=%g', m, b));
end
xlabel('Time (s)'); ylabel('v');
legend; title('Parameter sweep');
