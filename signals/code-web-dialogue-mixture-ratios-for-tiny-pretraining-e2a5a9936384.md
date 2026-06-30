# Code/web/dialogue mixture ratios for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384`
Run ID: `code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384-20260630T023924028677+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c0250eb2d34

## What looked useful

Balanced_33_33_34 ranked first by aggregate mean loss (1.1901) and worst-domain loss (1.3953). Web-heavy, code-heavy, and dialogue-heavy ratios each won their own domain but had substantially worse cross-domain losses.

## Boundaries and scale limits

The run used synthetic template-generated corpora, next-character validation, a sub-2M-parameter toy Transformer, 260 optimization steps per ratio, and 3 seeds. It does not validate real corpora, BPE tokenization, downstream tasks, larger models, or longer pretraining.

## Claim scope

In a controlled synthetic structured-data proxy with a tiny character-level causal Transformer, equal-ish web/code/dialogue mixing produced the best aggregated mean validation loss and worst-domain validation loss across 3 deterministic seeds; domain-heavy mixtures specialized on their own domain but paid large cross-domain loss.

## Why it stopped

Closed as a useful no-paper proxy result: the evidence is reproducible and mechanism-informative, but synthetic next-character validation is not direct enough for a publication-grade pretraining mixture claim.

## Recommended next action

Run the same seven-ratio sweep on small real public samples, for example WikiText-style prose, permissively licensed Python snippets, and dialogue data, using a shared BPE tokenizer and the same fixed-token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny mixture confirmation for code/web/dialogue ratios
- Success threshold: Balanced or near-balanced mixture ranks first on worst-domain validation loss in at least 2 of 3 seeds and is within 3% of the best mean validation loss.
- Stop condition: Stop if real-corpus setup cannot fit a sub-30-minute local run, or if two seeds show a non-balanced ratio beating balanced on both mean and worst-domain validation loss by at least 5%.

## Evidence references

- Artifact root: `<local-path>/projects/code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
