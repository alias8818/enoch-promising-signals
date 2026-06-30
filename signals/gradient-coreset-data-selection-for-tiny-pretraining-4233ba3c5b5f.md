# Gradient Coreset Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-coreset-data-selection-for-tiny-pretraining-4233ba3c5b5f`
Run ID: `gradient-coreset-data-selection-for-tiny-pretraining-4233ba3c5b5f-20260605T044221299539+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

Gradient coreset selection had the best full-pool gradient approximation and the lowest 8-seed mean validation loss: 2.8439 versus random 2.8838, top-loss 2.8791, and embedding diversity 2.8692. It won 7/8 paired seeds against each baseline.

## Boundaries and scale limits

Tiny Transformer only; byte-level tokenization; one corpus; small candidate pool; short training horizon; static one-shot gradients; no GPT-2-small-class, long-run, multi-corpus, tokenizer-level, or dynamic-refresh validation.

## Claim scope

On a small WikiText-2 byte-level tiny causal LM benchmark with 384 candidate sequences, 64 selected sequences, and 300 optimizer steps, one-shot output-head gradient mean matching selected subsets that improved held-out validation loss versus random, top-loss, and embedding-diversity baselines.

## Why it stopped

Local evidence is a useful small-scale direct signal, but it is not broad or durable enough for a paper-grade validation.

## Recommended next action

Run a bounded deepen follow-up with a tokenizer-based GPT-2-small-class or parameter-matched model, larger candidate pools, dynamic gradient refresh, and at least three corpora before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-scale dynamic gradient coreset selection for small LM pretraining
- Success threshold: Gradient coreset improves mean validation loss by at least 1 percent versus random and wins at least 70 percent of paired seeds or corpus runs, while matching or improving gradient-alignment diagnostics.
- Stop condition: Stop if gradient coreset fails to beat random on at least two of three corpora or if dynamic refresh erases the advantage relative to simpler baselines.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-data-selection-for-tiny-pretraining-4233ba3c5b5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
