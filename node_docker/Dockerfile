# Use a Node.js base image
FROM node:20

# Set the working directory
WORKDIR /usr/src/app

# Copy the application code
COPY app.js .

# Install dependencies (if needed, uncomment the next two lines)
# COPY package*.json ./
# RUN npm install

# Expose the application's port
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]
