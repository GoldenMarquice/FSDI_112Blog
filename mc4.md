# Mini Challenge 4

## Override the password reset templates

### Acceptance Criteria
1. Test the current flow by going to `http://127.0.0.1:8000/accounts/password_reset`
1.1. Follow the entire process to take note of the text in each of the template files
2. Once you understand the full flow, begin overriding each template, by covering:
2.1. Email request form: `registration/password_reset_form.html`
2.2.1. Email subject: `registration/password_reset_subject.txt`
2.2.2. Email body: `registration/password_reset_email.html`
2.2. Email sent template: `registration/password_reset_done.html`
2.3. New password form: `registration/password_reset_confirm.html`
2.4. Process complete template: `registration/password_reset_complete.html`
3. Change the `EMAIL_BACKEND` setting and test the entire flow.