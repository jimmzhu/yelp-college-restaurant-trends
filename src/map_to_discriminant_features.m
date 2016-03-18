x_train = csvread('../data/businesses-train.csv');
x_test = csvread('../data/businesses-test.csv');
[n_train, ~] = size(x_train);
[n_test, ~] = size(x_test);

dist_threshold = 5.2;
y_train = x_train(:,end) < dist_threshold;
y_test = x_test(:,end) < dist_threshold;

checkins_train = x_train(:,1:56);
checkins_test = x_test(:,1:56);
checkins_discriminant = fisher_lda(checkins_train, y_train);
z_checkins_train = checkins_train * checkins_discriminant;
z_checkins_test = checkins_test * checkins_discriminant;

categories_train = x_train(:,57:end-1);
categories_test = x_test(:,57:end-1);
categories_discriminant = fisher_lda(categories_train, y_train);
z_categories_train = categories_train * categories_discriminant;
z_categories_test = categories_test * categories_discriminant;

subtopics_train = csvread('../data/subtopics_vector_train.csv');
subtopics_test = csvread('../data/subtopics_vector_test.csv');
[subtopics_discriminant, mu_x_yes_subtopics, mu_x_no_subtopics] = ...
  fisher_lda(subtopics_train, kron(y_train, [1; 1; 1]), 'sparse');
z_subtopics_train = subtopics_train * subtopics_discriminant;
z_subtopics_test = subtopics_test * subtopics_discriminant;

z_train = ...
  [z_checkins_train z_categories_train reshape(z_subtopics_train, [3 n_train])'];
z_test = ...
  [z_checkins_test, z_categories_test, reshape(z_subtopics_test, [3 n_test])'];

csvwrite('../data/z_businesses_train.csv', [z_train, x_train(:,end)]);
csvwrite('../data/z_businesses_test.csv', [z_test, x_test(:,end)]);

save z_businesses.mat z_train y_train z_test y_test
save discriminants.mat checkins_discriminant categories_discriminant subtopics_discriminant
