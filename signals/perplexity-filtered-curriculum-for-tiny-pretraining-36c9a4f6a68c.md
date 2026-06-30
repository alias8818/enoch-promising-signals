# Perplexity-filtered curriculum for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtered-curriculum-for-tiny-pretraining-36c9a4f6a68c`
Run ID: `perplexity-filtered-curriculum-for-tiny-pretraining-36c9a4f6a68c-20260609T142400834893+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ae0acf3e7260

## What looked useful

Teacher perplexity separated clean from noisy synthetic documents, and filtering to low-PPL documents improved tiny LM held-out clean perplexity in all five seeds. The gain exceeded a same-size random filter control, indicating the signal comes from teacher-PPL selection rather than fewer training documents alone.

## Boundaries and scale limits

Synthetic corpus only; no natural text, transformer student, pretrained-LM teacher scoring, realistic token budget, or convergence-scale training. The result supports an early-training mechanism but is not broad or paper-ready validation.

## Claim scope

In a synthetic noisy-corpus setup with a NumPy tiny context language model, smoothed-bigram teacher perplexity, five seeds, and a fixed 24k-token early-training budget, low teacher-perplexity filtering improved clean held-out perplexity by 5.2% versus random-all and 4.9% versus a same-size random-filter control.

## Why it stopped

Current run produced a useful synthetic mechanism signal, but it is not paper-ready because the evidence is toy-scale and proxy-scored rather than natural-corpus transformer pretraining.

## Recommended next action

Run a bounded deepen follow-up on a real small text corpus with a tiny transformer or GPT-2-small-class baseline and teacher perplexity from an actual checkpoint; require at least 2% validation-PPL improvement over both random-all and same-size random-filter controls across at least three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer validation of teacher-perplexity filtering
- Success threshold: Low-PPL filtering or easy-to-hard ordering reduces validation perplexity by at least 2% versus both random-all and same-size random-filter controls across at least three seeds without degrading held-out test perplexity.
- Stop condition: Stop as unsupported if the best teacher-PPL schedule fails to beat both controls by 2% mean validation perplexity or if gains appear in only one seed.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-curriculum-for-tiny-pretraining-36c9a4f6a68c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
