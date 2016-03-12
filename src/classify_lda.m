gamma = 0.01
dist_thresholds = 0.5:0.1:5;
total_thresholds = length(dist_thresholds);

x_train = csvread('../data/businesses-train.csv'); % (:,[1:56, end]);
x_test = csvread('../data/businesses-test.csv');   % (:,[1:56, end]);
x_data_sets = { x_train, x_test };
[~, d_plus_1] = size(x_train);
d = d_plus_1 - 1;

p_errors = { zeros(1, total_thresholds), zeros(1, total_thresholds) };
lda_discriminants = zeros(d, total_thresholds);
p_yes = zeros(1, total_thresholds);
p_no = zeros(1, total_thresholds);
for set_index = 1:length(x_data_sets)
  x_data_set = x_data_sets{set_index};
  [total_x, ~] = size(x_data_set);

  for i = 1:total_thresholds
    dist_threshold = dist_thresholds(i);

    x_yes = x_data_set(x_data_set(:,end) < dist_threshold, 1:end-1);
    x_no  = x_data_set(x_data_set(:,end) >= dist_threshold, 1:end-1);
    [total_yes, ~] = size(x_yes);
    [total_no, ~]  = size(x_no);

    % center the data (using training set mu_x_center)
    if set_index == 1
      mu_x_center = (mean(x_yes) + mean(x_no)) / 2;
      p_yes(i) = total_yes / total_x;
      p_no(i) = total_no / total_x;
    end
    x_yes = x_yes - repmat(mu_x_center, [total_yes, 1]);
    x_no  = x_no - repmat(mu_x_center, [total_no, 1]);

    if set_index == 1
      % mean and covariance
      mu_x_yes = mean(x_yes)';
      mu_x_no  = mean(x_no)';
      Sigma_x_yes = cov(x_yes);
      Sigma_x_no  = cov(x_no);

      % get discriminant vector
      Sw = Sigma_x_yes + Sigma_x_no + gamma*eye(d);
      [~, ~, V] = svd(Sw \ (mu_x_yes - mu_x_no)*(mu_x_yes - mu_x_no)');
      lda_discriminants(:,i) = V(:,1);
    end

    % map features onto discriminant vector
    z_yes = (x_yes * lda_discriminants(:,i))';
    z_no  = (x_no * lda_discriminants(:,i))';

    if set_index == 1
      mu_z_yes = mean(z_yes, 2);
      mu_z_no  = mean(z_no, 2);
      Sigma_z_yes = cov(z_yes);
      Sigma_z_no  = cov(z_no);
    end

    z_yes_centered = z_yes - repmat(mu_z_yes, [1, total_yes]);
    z_no_centered  = z_no - repmat(mu_z_no, [1, total_no]);
    mahalanobis_z_yy = diag(z_yes_centered' * (Sigma_z_yes \ z_yes_centered)) ...
                     + log(det(Sigma_z_yes)) - 2*log(p_yes(i));
    mahalanobis_z_yn = diag(z_yes_centered' * (Sigma_z_no \ z_yes_centered)) ...
                     + log(det(Sigma_z_no)) - 2*log(p_no(i));

    mahalanobis_z_ny  = diag(z_no_centered' * (Sigma_z_yes \ z_no_centered)) ...
                      + log(det(Sigma_z_yes)) - 2*log(p_yes(i));
    mahalanobis_z_nn  = diag(z_no_centered' * (Sigma_z_no \ z_no_centered)) ...
                      + log(det(Sigma_z_no)) - 2*log(p_no(i));

    p_errors{set_index}(i) = (sum(mahalanobis_z_yn < mahalanobis_z_yy) ...
                           + sum(mahalanobis_z_ny < mahalanobis_z_nn)) / total_x;
  end
end

figure(1);
plot(dist_thresholds, p_yes, 'g', dist_thresholds, p_no, 'm'); hold on;
plot(dist_thresholds, p_errors{1});
plot(dist_thresholds, p_errors{2}, 'r'); hold off;
title('Error rate vs. distance threshold, Gaussian linear discriminant classifier');
xlabel('Chosen distance threshold (mi)');
ylabel('Probability of error');
legend('Probability within threshold', 'Probability outside threshold', ...
       'Training set', 'Test set');
