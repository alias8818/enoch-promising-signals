# Suffix N-Gram Drafting with Anchor Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-drafting-with-anchor-verification-bed34f6d6f74`
Run ID: `suffix-n-gram-drafting-with-anchor-verification-bed34f6d6f74-20260628T195901926422+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a3c7fc187826

## What looked useful

Sparse anchors gave the intended verifier-check reduction only when they accepted hidden interior errors. On template traces the best-cost setting reached 0.1523 verifier checks per accepted token but false-accepted 78.9% of accepted spans; adversarial-anchor traces reached 0.2991 checks/token but false-accepted 33.5% of spans. Zero-false-accept settings collapsed to full draft-token checking or no useful drafting.

## Boundaries and scale limits

No real neural language model, tokenizer, serving stack, or natural corpus latency measurement was run. Evidence is limited to CPU-only synthetic corpora with 60k train tokens and 30k test tokens per corpus across 108 configurations.

## Claim scope

Bounded deterministic proxy over synthetic token streams: suffix n-gram drafting can reduce verifier checks on repetitive data, but sparse anchor-only verification does not preserve exact accepted-token correctness.

## Why it stopped

Proxy evidence is an early falsification of sparse anchor verification as a correctness-preserving exact decoding method, not a full real-LM validation.

## Recommended next action

Stop this no-paper run; if pursued, implement the same anchor-verification test against a real LM verifier with a full-token verification control and adversarial interior-token prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM anchor verification falsification with full-token control
- Success threshold: At least 10k real-LM draft spans with sparse anchors showing either zero false accepts at a verifier-call reduction greater than 20%, or a reproducible nonzero hidden-error rate that confirms the proxy warning.
- Stop condition: Stop if sparse anchors produce any hidden accepted-token error under an exact-decoding claim, or if zero-error settings require verifying every drafted token.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-drafting-with-anchor-verification-bed34f6d6f74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
