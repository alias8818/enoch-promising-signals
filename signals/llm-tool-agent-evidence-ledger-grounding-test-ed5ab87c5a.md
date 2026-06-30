# LLM Tool-Agent Evidence Ledger Grounding Test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-tool-agent-evidence-ledger-grounding-test-ed5ab87c5a`
Run ID: `llm-tool-agent-evidence-ledger-grounding-test-ed5ab87c5a-20260522T143404376368+0000`

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

- Parent run decision: Evidence-Ledger Agent Loop: enoch://control-plane/projects/evidence-ledger-agent-loop-c8895b9488e6/runs/evidence-ledger-agent-loop-c8895b9488e6-20260522T135234636955+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/579f753113a8

## What looked useful

Qwen2.5-1.5B ledger improved answer accuracy from 0.833 to 0.900, citation validity from 0.767 to 1.000, and reduced unsupported failures from 0.733 to 0.533; Qwen2.5-0.5B failed ledger compliance and worsened unsupported failures from 0.833 to 0.900.

## Boundaries and scale limits

Synthetic snippets only; retrieved evidence was pre-supplied rather than obtained by a live agent; deterministic rule scoring; two Qwen model sizes; no real benchmark, human support labels, or production tool-agent loop.

## Claim scope

In a 30-case synthetic tool-evidence QA test, an explicit evidence-ledger prompt improved grounding for Qwen2.5-1.5B-Instruct when the model followed the ledger format, but did not help Qwen2.5-0.5B-Instruct.

## Why it stopped

Tier 1 controlled direct test completed; evidence is a useful mechanism signal but remains synthetic, small, model-dependent, and not paper-positive.

## Recommended next action

Run a bounded deepen follow-up on a real document-grounded QA benchmark with live retrieval/tool traces, claim-level support labels, and at least three model families before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Benchmark Evidence Ledger Grounding Confirmation
- Success threshold: Ledger condition reduces unsupported claim rate by >=15 percentage points versus baseline, answer accuracy drops by <=2 percentage points, and the effect holds for at least two of three tested model families.
- Stop condition: Stop if ledger compliance is below 90% on two model families or if unsupported-claim reduction is below 5 percentage points with any accuracy loss after 100 labeled cases.

## Evidence references

- Artifact root: `<local-path>/projects/llm-tool-agent-evidence-ledger-grounding-test-ed5ab87c5a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
