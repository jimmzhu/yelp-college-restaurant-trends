load lda_discriminant.mat

dist_threshold = 5.2;
x_yes = x_train(x_train(:,end) < dist_threshold, 1:end-1);
x_no  = x_train(x_train(:,end) >= dist_threshold, 1:end-1);
[total_yes, ~] = size(x_yes);
[total_no, ~]  = size(x_no);

mu_x_yes = mean(x_yes);
mu_x_no = mean(x_no);

% categories
categories_discriminant = lda_discriminant_52(57:end-3);
[~, category_indices] = sort(abs(categories_discriminant), 'descend');
top_categories = category_indices(1:11);
top_categories = category_indices(category_indices(1:11) ~= 9);
category_labels = { ...
  'Coffee & Tea', ...
  'Food Trucks', ...
  'Bakeries', ...
  'Cafes', ...
  'Specialty Food', ...
  'Grocery', ...
  'Beer, Wine & Spirits', ...
  'Convenience Stores', ...
  'Sandwiches', ...
  'Gas & Service Stations' ...
};

figure(2);
subplot(2,2,2);
bar(1:10, diag(total_yes*mu_x_yes(top_categories + 56)), 'stacked');
axis([0 11 0 800]);
title('Mean categories, within 5.2mi of college');
xlabel('Categories');
ylabel('Number of occurrences');

subplot(2,2,4);
bar(1:10, diag(total_no*mu_x_no(top_categories + 56)), 'stacked');
axis([0 11 0 800]);
title('Mean categories, outside 5.2mi of college');
xlabel('Categories');
ylabel('Number of occurrences');

subplot(2,2,[1 3]);
bar(1:10, diag(categories_discriminant(top_categories)), 'stacked');
axis([0 11 -0.15 0.15]);
title('Discriminant categories');
xlabel('Categories');
ylabel('Category discriminant component');
legend(category_labels{:}, 'Location', 'southoutside');
