# Direct Ledger-Backed Recall Test for a Local 1B Tool Agent

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-ledger-backed-recall-test-for-a-local-1b-tool-agent-366053c951`
Run ID: `direct-ledger-backed-recall-test-for-a-local-1b-tool-agent-366053c951-20260523T164652741354+0000`

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

- Parent run decision: Structured Evidence Ledger for 1B Local Tool Agents: enoch://control-plane/projects/structured-evidence-ledger-for-1b-local-tool-agents-8c3ab57aa984/runs/structured-evidence-ledger-for-1b-local-tool-agents-8c3ab57aa984-20260523T153104780259+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d616f470598f

## What looked useful

Direct Tier 1 evidence supports controller-mediated ledger-backed recall as a mechanism for exact synthetic memory retrieval in a local 1B-class agent, but it does not support autonomous prompt-only tool-call initiation by the model.

## Boundaries and scale limits

Single local 1.5B-class model, 24 trials per condition, synthetic exact-subject queries, deterministic controller-mediated lookup, no noisy retrieval, no multi-session persistence, no adversarial distractors, and no multi-model replication.

## Claim scope

On a deterministic 80-row synthetic append-only ledger, Qwen/Qwen2.5-1.5B-Instruct achieved 24/24 exact recall when an external controller supplied the matching ledger row, while no-ledger and wrong-ledger controls were 0/24. Prompt-only self-initiation of the ledger_search tool was 0/24.

## Why it stopped

Tier 1 direct test completed with useful mechanism support but mixed hypothesis status; the result is no-paper because autonomous self tool use failed and the successful condition depends on deterministic orchestration.

## Recommended next action

Run a bounded deepen test using a native tool/function-calling interface or parser wrapper for 1B-class models, requiring self-initiated ledger_search calls rather than deterministic controller lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native Tool-Call Ledger Recall for Local 1B Agents
- Success threshold: Native/self-initiated ledger_search condition reaches >=80% exact-match accuracy and >=80% valid tool-call rate, with no-ledger and wrong-ledger controls <=20%.
- Stop condition: Stop as unsupported if valid self-initiated tool-call rate remains below 50% after prompt/parser tuning on two 1B-class models or if controls exceed 20% exact-match accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/direct-ledger-backed-recall-test-for-a-local-1b-tool-agent-366053c951`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
