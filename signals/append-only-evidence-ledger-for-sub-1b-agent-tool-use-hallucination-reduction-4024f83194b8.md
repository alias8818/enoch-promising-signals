# Append-Only Evidence Ledger for Sub-1B Agent Tool-Use Hallucination Reduction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `append-only-evidence-ledger-for-sub-1b-agent-tool-use-hallucination-reduction-4024f83194b8`
Run ID: `append-only-evidence-ledger-for-sub-1b-agent-tool-use-hallucination-reduction-4024f83194b8-20260516T094246169408+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/26a54cf52b91

## What looked useful

Across five seeds of 16 answerable and 16 missing tasks each, the ledger condition increased overall hallucinated-answer rate by 11.875 percentage points, missing-answer hallucination by 12.5 points, and unsupported requester-guess copying by 26.875 points relative to the prose transcript baseline.

## Boundaries and scale limits

Single sub-1B model, synthetic single-turn final-answer tasks, fixed tool observations in prompt, no interactive tool calls, no external ledger verifier, no real-world agent traces.

## Claim scope

On a synthetic paired final-answer benchmark using Qwen/Qwen2.5-0.5B-Instruct, representing identical tool observations as a prompt-only append-only evidence ledger did not reduce tool-use hallucination versus a prose tool transcript.

## Why it stopped

Proxy/local early falsification: prompt-only append-only ledger formatting did not reduce hallucination and was worse than the matched prose transcript baseline on key unsupported-answer metrics.

## Recommended next action

Stop this prompt-only ledger line as no-paper evidence; run a bounded deepen follow-up that adds an external ledger verifier/rejection gate on the same benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Enforced Evidence Ledger Validator for Sub-1B Tool-Use Answers
- Success threshold: Ledger-plus-verifier reduces missing-answer hallucination by at least 25 percentage points versus prose_trace without reducing answerable exact rate by more than 5 percentage points across at least five seeds.
- Stop condition: Stop if verifier reduces hallucination only by converting most answerable cases to UNKNOWN, or if missing-answer hallucination remains within 5 percentage points of the prose_trace baseline.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-sub-1b-agent-tool-use-hallucination-reduction-4024f83194b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
