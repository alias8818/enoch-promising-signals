# Embedding-Contrastive Filtering for Tiny Pretraining Data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-contrastive-filtering-for-tiny-pretraining-data-304cb65fda20`
Run ID: `embedding-contrastive-filtering-for-tiny-pretraining-data-304cb65fda20-20260602T154646466994+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8035c5b031d9

## What looked useful

Relevance purity was not enough: contrastive selected 94.0% target documents but had mean target perplexity 3.540 versus random 2.187; contrastive+MMR selected 94.3% target documents but still had perplexity 2.819. Oracle target selection reached 1.265, showing the metric could reward good target coverage.

## Boundaries and scale limits

Synthetic corpus, generated labels, character-level GRU, hashed n-gram embeddings, 5 seeds, 120 selected documents per seed, 220 update steps per method. This does not validate or refute semantic embeddings, real web corpora, token-budgeted selection, GPT-class transformer pretraining, or downstream transfer.

## Claim scope

In a controlled synthetic tiny-pretraining proxy with hashed character n-gram embeddings and a small character GRU, naive embedding-contrastive filtering increased target-document purity and beat positive-only similarity, but worsened held-out target perplexity versus random selection; a simple MMR diversity penalty reduced but did not remove the gap.

## Why it stopped

Proxy early falsification rather than full validation: the direct trained-LM metric failed versus random despite high relevance purity, while the oracle control showed good selection can improve the metric.

## Recommended next action

Stop this run as a proxy early falsification of naive contrastive filtering; the next bounded test should use token-budgeted semantic embeddings with explicit coverage/diversity controls on a small real corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Budgeted Semantic Contrastive Filtering with Coverage Controls
- Success threshold: Contrastive plus coverage/diversity improves mean target perplexity by at least 10% versus random and positive-only baselines, with no seed showing worse perplexity than random by more than 5%.
- Stop condition: Stop if contrastive plus coverage/diversity fails to beat random on mean target perplexity or if gains depend only on documents-per-budget artifacts rather than token-matched content quality.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-contrastive-filtering-for-tiny-pretraining-data-304cb65fda20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
