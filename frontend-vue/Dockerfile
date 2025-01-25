# Use Node 18 (LTS version) for better stability
FROM node:18

WORKDIR /frontend-vue

# Copy package.json and package-lock.json
COPY frontend-vue/package*.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY frontend-vue/ .

# # Build the Vue app
# RUN npm run build

EXPOSE 4173

CMD ["npm", "run", "dev", "serve", "--", "--host", "0.0.0.0"]