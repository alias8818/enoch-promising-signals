# Tokenizer-accurate small-LLM evidence ledger under natural-language trace pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tokenizer-accurate-small-llm-evidence-ledger-under-natural-88e9a27ca7`
Run ID: `tokenizer-accurate-small-llm-evidence-ledger-under-natural-88e9a27ca7-20260605T212255295102+0000`

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

- Parent run decision: Evidence ledger for small agent reliability under context pressure: enoch://control-plane/projects/evidence-ledger-for-small-agent-reliability-under-context-pressure-7ebe34a7ab42/runs/evidence-ledger-for-small-agent-reliability-under-context-pressure-7ebe34a7ab42-20260605T195318368531+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/92f395025fa0

## What looked useful

Tokenizer-accurate packing materially reduced destructive context truncation and preserved answer recovery under natural-language trace pressure, but prompt-only FLAN-T5-small did not reliably emit exact evidence IDs, leaving the full evidence-ledger claim mixed and not paper-ready.

## Boundaries and scale limits

Single small seq2seq model, synthetic QA ledgers, one tokenizer, prompt-only citation request, 48-item tokenization-stress test plus 24-item natural-language control; no real retrieval corpus, no training, no multi-model robustness, and exact citation grounding did not work.

## Claim scope

In a controlled synthetic FLAN-T5-small benchmark with strict 256-token inputs, tokenizer-accurate evidence-ledger packing preserved answer-relevant evidence and achieved 91.7%-95.8% answer accuracy where character-approximate or all-evidence truncation arms achieved 0.0% answer accuracy.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal but failed the stricter evidence-ledger citation requirement; this is no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with a stronger small instruction model or citation-constrained decoder and require joint answer+citation accuracy, not answer-only recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Citation-constrained tokenizer-accurate ledger test on small instruction models
- Success threshold: Tokenizer-accurate plus citation constraint reaches at least 70% joint answer+citation accuracy and improves by at least 20 percentage points over the best approximate/truncation baseline on both natural and tokenizer-stress conditions.
- Stop condition: Stop if citation-constrained decoding or the stronger small model remains below 40% joint answer+citation accuracy, or if the tokenizer-accurate advantage disappears under a non-truncated fair budget.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-accurate-small-llm-evidence-ledger-under-natural-88e9a27ca7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
