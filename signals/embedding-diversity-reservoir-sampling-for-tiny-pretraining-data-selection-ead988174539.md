# Embedding-diversity reservoir sampling for tiny pretraining data selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-diversity-reservoir-sampling-for-tiny-pretraining-data-selection-ead988174539`
Run ID: `embedding-diversity-reservoir-sampling-for-tiny-pretraining-data-selection-ead988174539-20260518T201344120273+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/62eeb01088ca

## What looked useful

Pure embedding diversity reliably improved coverage metrics, but downstream tiny-pretraining utility was budget-dependent: 256 chunks improved NLL by 0.0266 versus random, while 64 chunks was 0.0055 worse than random. Diversity alone is therefore not sufficient as a paper-ready tiny data selector, but it is a concrete mechanism worth testing with quality weighting and exact-token transformer controls.

## Boundaries and scale limits

This run did not test GPT-2/BPE transformer pretraining, web-scale corpora, foundation-model embeddings, exact equal unique-token budgets, or long training. Evidence is limited to two small local budgets, three training seeds, one real text corpus, and a small byte-level GRU proxy.

## Claim scope

On 20 Newsgroups fixed-size text chunks with local TF-IDF/SVD embeddings and a small byte-level GRU LM, embedding-diversity reservoir sampling improves embedding tail coverage/redundancy and improves held-out LM NLL at a 256-chunk budget, but not at a stricter 64-chunk budget.

## Why it stopped

Proxy-to-direct local evidence is mixed rather than paper-positive: the sampler improves embedding coverage and the 256-chunk LM result, but fails the 64-chunk stress test.

## Recommended next action

Run a bounded deepen follow-up with exact-token BPE-transformer pretraining and a quality-weighted diversity reservoir; stop this run as a no-paper useful signal because the direct LM metric is mixed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-token transformer test of quality-weighted embedding diversity sampling
- Success threshold: Quality-weighted diversity must beat random reservoir by at least 0.02 held-out NLL at both 64-ish and 256-ish chunk budgets, with no budget showing a regression larger than 0.005 NLL and with better p95 embedding coverage than random.
- Stop condition: Stop if pure or quality-weighted diversity fails to beat random on held-out NLL in two budgets or if improvements vanish when exact token budgets and multiple stream orders are enforced.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-diversity-reservoir-sampling-for-tiny-pretraining-data-selection-ead988174539`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
