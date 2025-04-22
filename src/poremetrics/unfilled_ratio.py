import numpy as np
import cv2
def unfilled_ratio(img):
    if img.dtype != np.uint8:
        img = img.astype(np.uint8)

    # Apply threshold to get binary image
    _, binary = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return 0
    
    # Find the largest contour (assuming it's the main object)
    main_contour = max(contours, key=cv2.contourArea)
    
    # Calculate total area within the outer contour
    total_area = cv2.contourArea(main_contour)

    # Calculate area of holes
    holes_area = 0
    print(len(contours))
    if hierarchy is not None:
        for i, h in enumerate(hierarchy[0]):
            # If this contour has a parent (meaning it's a hole)
            if h[3] >= 0:  # h[3] is the index of the parent contour
                holes_area += cv2.contourArea(contours[i])
    
    # Calculate ratio
    if total_area == 0:
        return 0
    unfilled_ratio = holes_area / total_area
    return unfilled_ratio

# # %%
# if __name__ =="__main__":
#     # Create visualization
#     visualization = img.copy()
#     # Draw main contour in green
#     cv2.drawContours(visualization, [main_contour], -1, (0, 255, 0), 2)
#     # Draw holes in red
#     for i, h in enumerate(hierarchy[0]):
#         if h[3] >= 0:  # If it's a hole
#             cv2.drawContours(visualization, [contours[i]], -1, (0, 0, 255), 2)
    
#     Add text with measurements
#     cv2.putText(visualization, f'Total Area: {total_area:.0f}', (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#     cv2.putText(visualization, f'Holes Area: {holes_area:.0f}', (10, 60),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#     cv2.putText(visualization, f'Ratio: {fill_ratio:.3f}', (10, 90),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#     cv2.imshow('fill visualization',visualization)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()