# Use a different Node.js base image
FROM node:14 as build

# Set working directory
WORKDIR /app

# Copy everything to the /app directory
COPY . /app

# Install and cache dependencies
RUN yarn install

# Build the project for production
RUN yarn build

# Set up production environment
FROM nginx:alpine

# # Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/nginx.conf usr/share/

# Copy your custom Nginx configuration
COPY nginx/nginx.conf /etc/nginx/conf.d/

# Copy the build folder from React to the root of nginx (www)
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 5000 to the outer world
EXPOSE 5000

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
