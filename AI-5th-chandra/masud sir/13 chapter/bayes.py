def bayes_rule(prior_A, likelihood_B_given_A, marginal_B):
    # Calculate the posterior probability P(A|B)
    posterior_A_given_B = (likelihood_B_given_A * prior_A) / marginal_B
    return posterior_A_given_B

# Example values
prior_A = 0.01  # Prior probability, P(A)
likelihood_B_given_A = 0.8  # Likelihood, P(B|A)
marginal_B = 0.05  # Evidence, P(B)

# Calculate P(A|B)
posterior_A_given_B = bayes_rule(prior_A, likelihood_B_given_A, marginal_B)
print("P(A|B):", posterior_A_given_B)