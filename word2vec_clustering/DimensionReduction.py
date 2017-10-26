from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import numpy as np


class DimensionReduction:
    def PCA(self, vector, dim=3):
        pca = PCA(n_components=dim)
        result = pca.fit_transform(vector)

        print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))
        print('Average of Explained variations: {}'.format(np.sum(pca.explained_variance_ratio_)))
        # result = list()
        # for vec in projected_vec:
        #     result.append([format(vec[0], '.4f'), format(vec[1], '.4f'), format(vec[2], '.4f')])

        return result

    def TSNE(self, vector, dim=3):
        tsne = TSNE(n_components=dim, verbose=1)
        result = tsne.fit_transform(vector)

        # result = list()
        # for vec in projected_vec:
        #     result.append([format(vec[0], '.4f'), format(vec[1], '.4f'), format(vec[2], '.4f')])

        return result


if __name__ == "__main__":
    sample_vec = [[1,2,3,4,5], [6,4,3,6,3],[3,1,2,1,1]]
    dim_reduction = DimensionReduction()
    pca_result = dim_reduction.PCA(sample_vec)
    tsne_result = dim_reduction.TSNE(sample_vec)

    print("PCA Result: {0}".format(pca_result))
    print("T-SNE Result: {0}".format(tsne_result))