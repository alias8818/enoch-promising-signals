# Evidence-ledger enforcement on real multi-document QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-enforcement-on-real-multi-document-qa-52c675bb7e`
Run ID: `evidence-ledger-enforcement-on-real-multi-document-qa-52c675bb7e-20260612T093852484113+0000`

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

- Parent run decision: Evidence-Ledger Mandatory Agent Protocol: enoch://control-plane/projects/evidence-ledger-mandatory-agent-protocol-467f98b16b8c/runs/evidence-ledger-mandatory-agent-protocol-467f98b16b8c-20260611T150217624475+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Citation coverage alone is not a sufficient evidence-ledger enforcement boundary for real multi-document QA. The mechanism needs answer-to-evidence binding; under oracle answer binding, false accepts fell from 100% for answer-only and 20% for citation-only ledger to 0% on 1,200 controlled candidates.

## Boundaries and scale limits

No live LLM generation, no learned or NLI semantic verifier, no human equivalence adjudication, and only 200 validation examples. The answer-bound positive result uses gold answer labels and is not a deployed verifier result.

## Claim scope

On 200 HotpotQA distractor validation examples with programmatic candidate outputs, hash-addressed citation ledgers reject missing, partial, and wrong citations, but citation-only enforcement fails wrong-answer-with-correct-citation cases; oracle answer-bound enforcement passes the controlled threshold.

## Why it stopped

Tier 1 direct test completed; result is a no-paper useful signal because citation-only ledger enforcement was falsified and answer-bound enforcement was only oracle-controlled, not publication-grade.

## Recommended next action

Run a bounded LLM-in-the-loop HotpotQA follow-up where a small local instruction model emits answer-plus-ledger outputs and an automatic answer-to-evidence verifier replaces the oracle answer binding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-authored answer-bound evidence ledgers on HotpotQA
- Success threshold: On at least 100 HotpotQA validation examples, unsupported false accept rate is at least 50 percentage points lower than answer-only and supported correct-answer retention is at least 0.80.
- Stop condition: Stop if the verifier rejects more than 30% of clearly supported gold-equivalent answers or if unsupported false-accept reduction is below 20 percentage points on the first 50 examples.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-enforcement-on-real-multi-document-qa-52c675bb7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
