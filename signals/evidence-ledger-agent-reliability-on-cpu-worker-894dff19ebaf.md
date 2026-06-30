# Evidence-Ledger Agent Reliability on CPU Worker

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-on-cpu-worker-894dff19ebaf`
Run ID: `evidence-ledger-agent-reliability-on-cpu-worker-894dff19ebaf-20260620T102202216484+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a0ad0c6bd9

## What looked useful

The implemented verifier achieved 12/12 accuracy with 0 false accepts and 0 false rejects on 6 supported controls and 6 trap claims, compared with an accept-all baseline at 6/12 accuracy and 6 false accepts.

## Boundaries and scale limits

Synthetic structured facts only; no live LLM agent, no real tool traces, no natural-language entailment, no hidden corpus, no long-run or production benchmark validation.

## Claim scope

A deterministic fact-level evidence-ledger gate rejected all unsupported claims in a 12-claim synthetic local fixture while accepting all supported controls; this supports the mechanism at toy scaffold scale only.

## Why it stopped

Bounded synthetic proxy supports the ledger-gating mechanism but is insufficient for a paper or broad agent-reliability claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a blinded real tool-trace fixture with LLM-authored claims and the same false accept/reject metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded tool-trace evidence-ledger reliability fixture
- Success threshold: Ledger gate cuts false accepts by at least 50% relative to accept-all while keeping false rejects at or below 10% on supported claims.
- Stop condition: Stop if setup cannot produce blinded trace labels, or if ledger false rejects exceed 20% after the first 25 labeled claims.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-cpu-worker-894dff19ebaf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
