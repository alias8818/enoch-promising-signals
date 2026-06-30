# Bounded suffix-tree draft with no extra model weights

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-suffix-tree-draft-with-no-extra-model-weights-b84fef66e120`
Run ID: `bounded-suffix-tree-draft-with-no-extra-model-weights-b84fef66e120-20260619T142037736994+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/999e8a3b4411

## What looked useful

Bounded suffix copying is a plausible no-extra-weights draft source for repetitive/code-like contexts, with the iid control showing the gain is tied to repeated continuation structure rather than draft accounting.

## Boundaries and scale limits

Synthetic corpora only; no neural verifier, no real tokenizer/model decode loop, no quality metric, no trained speculative-draft baseline, and no wall-clock serving benchmark. CPU-only run completed in seconds and does not validate large-scale deployment.

## Claim scope

On deterministic synthetic repetitive token streams, an online bounded suffix-history index with no learned draft weights produced exact-match draft spans that reduced proxy verifier calls by 50.7% to 81.0%; on an iid word control it produced 0.0% reduction.

## Why it stopped

This run produced only proxy/synthetic evidence; it supports the mechanism but is not a full validation or paper-ready result.

## Recommended next action

Run a bounded real-verifier follow-up using GPT-2-small-class decoding on a small natural/code corpus, comparing suffix-history drafts against one-token decoding and a simple ngram draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-verifier bounded suffix-history drafting on small code and prose corpora
- Success threshold: At least 20% verifier-call reduction and at least 10% wall-clock decode speedup on one repetitive real corpus, with no output mismatch versus the verifier's greedy sequence.
- Stop condition: Stop if suffix-history drafts reduce verifier calls by less than 10% or wall-clock speed is not improved on both tested real corpora.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-suffix-tree-draft-with-no-extra-model-weights-b84fef66e120`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
