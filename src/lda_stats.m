load lda_discriminant.mat

dist_threshold = 5.2;
x_yes = x_train(x_train(:,end) < dist_threshold, 1:end-1);
x_no  = x_train(x_train(:,end) >= dist_threshold, 1:end-1);
[total_yes, ~] = size(x_yes);
[total_no, ~]  = size(x_no);

mu_x_yes = mean(x_yes);
mu_x_no = mean(x_no);

% checkins
checkins_yes_by_hour = zeros(8,7);
checkins_no_by_hour = zeros(8,7);
checkins_discriminant_by_hour = zeros(8,7);
for i = 1:8
  checkins_yes_by_hour(i,:) = mu_x_yes(i:8:56);
  checkins_no_by_hour(i,:) = mu_x_no(i:8:56);
  checkins_discriminant_by_hour(i,:) = lda_discriminant_52(i:8:56);
end

figure(2);
subplot(3,1,1);
bar(1:7, checkins_yes_by_hour');
axis([0.5 7.5 0 0.07]);
set(gca, 'XTickLabel', { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' });
title('Mean frequency of checkins, within 2mi of college');
xlabel('Checkin hours over the week');
ylabel('Checkin frequency');

subplot(3,1,2);
bar(1:7, checkins_no_by_hour');
axis([0.5 7.5 0 0.07]);
set(gca, 'XTickLabel', { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' });
title('Mean frequency of checkins, outside 2mi of college');
xlabel('Checkin hours over the week');
ylabel('Checkin frequency');

subplot(3,1,3);
bar(1:7, checkins_discriminant_by_hour');
set(gca, 'XTickLabel', { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' });
axis([0.5 7.5 -0.2 0.2]);
title('Discriminant frequency of checkins');
xlabel('Checkin hours over the week');
ylabel('Checkin frequency');
