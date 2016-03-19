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
checkin_labels = { ...
  '12am-7am', ...
  '7am-11am', ...
  '9am-1pm', ...
  '11am-3pm', ...
  '1pm-5pm', ...
  '5pm-8pm', ...
  '7pm-9pm', ...
  '9pm-12am'
};

figure(2);
subplot(4,1,1);
bar(1:7, checkins_yes_by_hour');
axis([0.5 7.5 0 0.07]);
set(gca, 'XTickLabel', { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' });
title('Mean frequency of checkins, within 5.2mi of college');
xlabel('Checkin hours over the week');
ylabel('Checkin frequency');

subplot(4,1,2);
bar(1:7, checkins_no_by_hour');
axis([0.5 7.5 0 0.07]);
set(gca, 'XTickLabel', { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' });
title('Mean frequency of checkins, outside 5.2mi of college');
xlabel('Checkin hours over the week');
ylabel('Checkin frequency');

subplot(4,1,3);
bar(1:7, checkins_discriminant_by_hour');
set(gca, 'XTickLabel', { 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' });
axis([0.5 7.5 -0.05 0.05]);
title('Discriminant frequency of checkins');
xlabel('Checkin hours over the week');
ylabel('Checkin discriminant');

subplot(4,1,4);
dummy = bar(1:7, checkins_discriminant_by_hour');
set(dummy, 'Visible', 'off');
axis off;
legend(checkin_labels{:}, 'Location', 'south' );
