# Exact-Anchor Retrieval vs Full-Context Long-Document QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-retrieval-vs-full-context-long-document-qa-1044cda0921c`
Run ID: `exact-anchor-retrieval-vs-full-context-long-document-qa-1044cda0921c-20260628T021607194789+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/795ee7683651

## What looked useful

Clean exact-anchor retrieval reached 100% accuracy over 200-query sweeps up to 20,000 records / 940,000 whitespace tokens with 174x to 17,407x context compression versus full-document input. Fixed-window truncation dropped to about 0.5%-1% accuracy at the longest setting. Injecting 10% single-character anchor corruption reduced anchor retrieval accuracy by roughly the same amount, identifying brittleness as the main practical risk.

## Boundaries and scale limits

Synthetic extraction benchmark only; no LLM generation, no public corpus, no semantic retrieval baseline, no adversarial citation formats, and no tokenizer/model-specific context accounting.

## Claim scope

In deterministic synthetic long documents where each question supplies a correct exact anchor, exact-anchor retrieval preserved answer accuracy while reducing per-query context from full-document scale to a roughly 54-token local window; fixed 8192-token truncation failed as documents grew.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-only and does not validate real long-document QA behavior.

## Recommended next action

Run a bounded real-corpus follow-up using exact citations or generated stable anchors, with LLM answer generation and equal answer scoring against long-context prompting and ordinary retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor retrieval with LLM answer generation on cited long-document QA
- Success threshold: At least 95% of long-context answer accuracy with at least 100x lower median input tokens, plus less than 5 percentage-point degradation under realistic anchor noise.
- Stop condition: Stop if anchor-window generation falls below 90% of long-context accuracy or anchor noise above 5% causes more than 10 percentage-point absolute accuracy loss without a simple fallback.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-vs-full-context-long-document-qa-1044cda0921c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
